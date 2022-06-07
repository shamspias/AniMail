from django.core.mail import send_mail


def recipient_string_to_list(recipient_list):
    """
    Convert String emails to list
    """
    # main_list = recipient_list.split('.com', '.net', 'info', '.me')
    main_list = recipient_list.split(',')
    return main_list


def recipient_csv_to_list(recipient_list):
    """
    take emails from csv file and transform into a list
    """
    pass


def send_mails(sender, subject, main_text, recipient_list):
    """
    Method to send mail
    """
    recipients_list = recipient_string_to_list(recipient_list)
    send_mail(subject, main_text, sender, recipients_list)
    return True
