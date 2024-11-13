from emails.tasks.send_email import send_email


class Email:

    @staticmethod
    def change_password_email():
        send_email.delay(
            subject="Reset Password",
            message="this is reset password mail"
        )

        return None
