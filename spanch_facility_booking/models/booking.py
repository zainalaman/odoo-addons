from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FacilityBooking(models.Model):
    _name = 'facility.booking'
    _description = 'Facility Booking'

    name = fields.Char(string='Booking Reference', required=True)
    facility_id = fields.Many2one('facility', string='Facility', required=True)
    user_id = fields.Many2one('res.users', string='Booked By', required=True, default=lambda self: self.env.user)
    
    start_datetime = fields.Datetime(string='Start Date/Time', required=True)
    end_datetime = fields.Datetime(string='End Date/Time', required=True)
    
    purpose = fields.Char(string='Purpose', required=True)
    attendees = fields.Integer(string='Number of Attendees', default=1)
    description = fields.Text(string='Description')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.constrains('start_datetime', 'end_datetime', 'facility_id', 'state')
    def _check_booking_overlap(self):
        """Prevent overlapping bookings for the same facility"""
        for booking in self:
            if booking.state in ['cancelled', 'completed']:
                continue
                
            if not booking.start_datetime or not booking.end_datetime:
                continue
                
            # Validate date order
            if booking.start_datetime >= booking.end_datetime:
                raise ValidationError("End date/time must be after start date/time.")
            
            # Check for overlapping bookings
            overlapping = self.search([
                ('id', '!=', booking.id),
                ('facility_id', '=', booking.facility_id.id),
                ('state', 'in', ['draft', 'confirmed']),
                ('start_datetime', '<', booking.end_datetime),
                ('end_datetime', '>', booking.start_datetime)
            ])
            
            if overlapping:
                overlap_names = [f"'{ov.name}'" for ov in overlapping]
                raise ValidationError(
                    f"This booking overlaps with existing booking(s) for {booking.facility_id.name}: " +
                    ", ".join(overlap_names) +
                    ". Please choose a different time or facility."
                )

    # Action methods - handle all states gracefully
    def action_confirm(self):
        """Confirm the booking - only works for draft bookings"""
        for booking in self:
            if booking.state != 'draft':
                continue
            # Check for overlaps before confirming
            booking._check_booking_overlap()
            booking.write({'state': 'confirmed'})
        return True

    def action_complete(self):
        """Mark booking as completed - only works for confirmed bookings"""
        for booking in self:
            if booking.state == 'confirmed':
                booking.write({'state': 'completed'})
        return True

    def action_cancel(self):
        """Cancel the booking - works for draft and confirmed bookings"""
        for booking in self:
            if booking.state in ['draft', 'confirmed']:
                booking.write({'state': 'cancelled'})
        return True