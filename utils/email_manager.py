"""
Email manager for WERBEAUTY.
Handles sending password reset and notification emails.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional


def send_password_reset_email(recipient_email: str, reset_token: str, recipient_name: str = "User") -> tuple[bool, str]:
    """
    Send a password reset email to the user.
    
    Args:
        recipient_email: Email address to send to
        reset_token: Temporary password reset token
        recipient_name: Name of the recipient
    
    Returns:
        Tuple of (success, message)
    """
    # Email configuration - Using Gmail SMTP
    # NOTE: For production, use environment variables or a config file
    sender_email = "werbeauty.app@gmail.com"  # Replace with your email
    sender_password = os.environ.get("EMAIL_PASSWORD", "")  # Use app-specific password
    
    if not sender_password:
        # For demo purposes, log the reset token
        print(f"\n{'='*60}")
        print(f"PASSWORD RESET REQUEST")
        print(f"{'='*60}")
        print(f"Recipient: {recipient_email}")
        print(f"Name: {recipient_name}")
        print(f"Reset Token: {reset_token}")
        print(f"\nTo enable actual email sending:")
        print(f"1. Set up a Gmail account for the app")
        print(f"2. Enable 2-factor authentication")
        print(f"3. Generate an app-specific password")
        print(f"4. Set EMAIL_PASSWORD environment variable")
        print(f"{'='*60}\n")
        
        return True, f"Password reset instructions sent to {recipient_email} (Check console for demo token)"
    
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = "🔒 Password Reset Request - WERBEAUTY"
        message["From"] = f"WERBEAUTY <{sender_email}>"
        message["To"] = recipient_email
        
        # Create HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="margin: 0; padding: 0; font-family: 'Arial', sans-serif; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);">
            <table role="presentation" style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td align="center" style="padding: 40px 20px;">
                        <table role="presentation" style="max-width: 600px; width: 100%; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border-radius: 24px; overflow: hidden; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);">
                            <!-- Header -->
                            <tr>
                                <td style="padding: 40px 40px 30px; text-align: center; background: linear-gradient(135deg, #B76E79, #d4a5ad);">
                                    <h1 style="margin: 0; color: white; font-size: 2rem; font-family: 'Playfair Display', serif;">WERBEAUTY</h1>
                                    <p style="margin: 10px 0 0; color: rgba(255, 255, 255, 0.9); font-size: 0.95rem;">Password Reset Request</p>
                                </td>
                            </tr>
                            
                            <!-- Content -->
                            <tr>
                                <td style="padding: 40px; color: rgba(255, 255, 255, 0.9); line-height: 1.6;">
                                    <p style="margin: 0 0 20px; font-size: 1.1rem;">Hello {recipient_name},</p>
                                    
                                    <p style="margin: 0 0 20px;">We received a request to reset your password for your WERBEAUTY account. If you didn't make this request, you can safely ignore this email.</p>
                                    
                                    <p style="margin: 0 0 30px;">Use the following temporary password to log in, then change it immediately in your profile settings:</p>
                                    
                                    <!-- Token Box -->
                                    <div style="background: rgba(183, 110, 121, 0.2); border: 2px solid #B76E79; border-radius: 12px; padding: 20px; margin: 0 0 30px; text-align: center;">
                                        <p style="margin: 0 0 10px; color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">Temporary Password:</p>
                                        <p style="margin: 0; color: #B76E79; font-size: 1.5rem; font-weight: bold; letter-spacing: 2px; font-family: 'Courier New', monospace;">{reset_token}</p>
                                    </div>
                                    
                                    <p style="margin: 0 0 20px; color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">⚠️ <strong>Important Security Notes:</strong></p>
                                    <ul style="margin: 0 0 30px; padding-left: 20px; color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">
                                        <li>This temporary password will expire in 1 hour</li>
                                        <li>Change your password immediately after logging in</li>
                                        <li>Never share your password with anyone</li>
                                        <li>If you didn't request this reset, contact our support team</li>
                                    </ul>
                                    
                                    <p style="margin: 0 0 10px;">Need help? Contact us at:</p>
                                    <p style="margin: 0; color: #B76E79;">📧 support@werbeauty.com</p>
                                </td>
                            </tr>
                            
                            <!-- Footer -->
                            <tr>
                                <td style="padding: 30px 40px; text-align: center; border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                    <p style="margin: 0 0 10px; color: rgba(255, 255, 255, 0.5); font-size: 0.85rem;">© 2025 WERBEAUTY. All rights reserved.</p>
                                    <p style="margin: 0; color: rgba(255, 255, 255, 0.4); font-size: 0.8rem;">Luxury Beauty Products | Premium Cosmetics</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        
        # Plain text alternative
        text_content = f"""
        WERBEAUTY - Password Reset Request
        
        Hello {recipient_name},
        
        We received a request to reset your password for your WERBEAUTY account.
        
        Your temporary password: {reset_token}
        
        Use this temporary password to log in, then change it immediately in your profile settings.
        
        Important:
        - This temporary password expires in 1 hour
        - Change your password after logging in
        - If you didn't request this, contact support@werbeauty.com
        
        Best regards,
        WERBEAUTY Team
        """
        
        # Attach both versions
        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        message.attach(part1)
        message.attach(part2)
        
        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        return True, f"Password reset instructions sent to {recipient_email}"
    
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False, f"Failed to send email. Please try again later or contact support."


def send_welcome_email(recipient_email: str, recipient_name: str) -> tuple[bool, str]:
    """
    Send a welcome email to new users.
    
    Args:
        recipient_email: Email address to send to
        recipient_name: Name of the recipient
    
    Returns:
        Tuple of (success, message)
    """
    # This is a placeholder for future implementation
    # Can be used to send welcome emails when users sign up
    return True, "Welcome email feature coming soon"
