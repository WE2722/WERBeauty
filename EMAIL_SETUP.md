# Email Configuration Guide for WERBEAUTY

## Overview
The forgot password feature sends password reset emails to users. The system uses Gmail SMTP by default.

## Demo Mode (Current Setup)
Without email configuration, the system works in **demo mode**:
- Temporary passwords are generated and displayed in the console/terminal
- All password reset functionality works normally
- Perfect for development and testing

## Production Setup (Optional)

To enable actual email sending, follow these steps:

### 1. Create a Gmail Account for the App
- Create a dedicated Gmail account for the application (e.g., werbeauty.app@gmail.com)
- This keeps app emails separate from personal accounts

### 2. Enable 2-Factor Authentication
1. Go to Google Account settings
2. Navigate to Security
3. Enable 2-Step Verification

### 3. Generate App-Specific Password
1. Go to Google Account → Security → 2-Step Verification
2. Scroll down to "App passwords"
3. Generate a new app password for "Mail"
4. Copy the 16-character password (e.g., "abcd efgh ijkl mnop")

### 4. Set Environment Variable

**Windows PowerShell:**
```powershell
$env:EMAIL_PASSWORD = "your-app-password-here"
```

**Windows Command Prompt:**
```cmd
set EMAIL_PASSWORD=your-app-password-here
```

**Linux/Mac:**
```bash
export EMAIL_PASSWORD=your-app-password-here
```

**For Permanent Setup (Windows):**
1. Search for "Environment Variables" in Windows
2. Add new system variable:
   - Name: `EMAIL_PASSWORD`
   - Value: Your app password

### 5. Update Sender Email (Optional)
Edit `utils/email_manager.py` line 21:
```python
sender_email = "your-email@gmail.com"  # Replace with your Gmail
```

## Testing the Feature

### Demo Mode Test:
1. Start the app: `python -m streamlit run app.py`
2. Go to Login page
3. Click "Forgot password?"
4. Enter any registered email
5. Check the console/terminal for the temporary password
6. Copy the temporary password
7. Use it to log in
8. Change your password in Profile → Security

### Production Mode Test (with EMAIL_PASSWORD set):
1. Follow steps 1-4 above
2. Check the email inbox for the password reset email
3. Use the temporary password from the email
4. Change your password in Profile → Security

## Security Features

✅ **Secure Token Generation**: Uses Python's `secrets` module  
✅ **Password Hashing**: Temporary passwords are hashed like regular passwords  
✅ **Expiration**: Temporary passwords expire after 1 hour  
✅ **Auto Cleanup**: Expired temporary passwords are automatically removed  
✅ **No Email Enumeration**: Doesn't reveal if an email exists in the system  
✅ **Warning System**: Users are warned to change temporary passwords immediately

## Email Template

The system sends a beautiful HTML email with:
- WERBEAUTY branding and styling
- Clear temporary password display
- Security instructions and warnings
- 1-hour expiration notice
- Support contact information

## Troubleshooting

**"Failed to send email"**
- Check your EMAIL_PASSWORD environment variable
- Verify 2-factor authentication is enabled
- Ensure app password is correct (no spaces)
- Check your Gmail account isn't locked

**"Temporary password has expired"**
- Request a new password reset
- Each temporary password is valid for only 1 hour

**Not receiving emails**
- Check spam/junk folder
- Verify EMAIL_PASSWORD is set correctly
- Check Gmail account status
- Try demo mode to verify the feature works

## Alternative Email Providers

To use other email providers (e.g., Outlook, custom SMTP):

Edit `utils/email_manager.py` lines 76-78:
```python
# For Gmail (default):
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

# For Outlook/Hotmail:
with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.starttls()

# For custom SMTP:
with smtplib.SMTP("your-smtp-server.com", 587) as server:
    server.starttls()
```

## Support

For issues or questions:
- Email: support@werbeauty.com
- GitHub: https://github.com/WE2722/WERBeauty

---

*Last updated: December 2025*
