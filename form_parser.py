def print_the_upload_form(data: dict):
    print("=" * 8, "Basic info about the employee:", "=" * 8)
    print("Name: ", data["name"])
    print("Employee ID: ", data["empId"])
    print("Location: ", data["location"])
    print("Designation: ", data["designation"])
    print("Department: ", data["department"])
    print("Purpose of Visit: ", data["purposeOfVisit"])
    print()
    print("=" * 8, "Travel details:", "=" * 8)
    print("Length of travels: ", len(data["travels"]))
    print()

    for c, i in enumerate(data["travels"]):
        print("=" * 8, "Travel #", c + 1, "=" * 8)
        print("Travel ID: ", i["travelId"])
        print("Travel date: ", i["travelDate"])
        print("Travel from: ", i["travelFrom"])
        print("Travel to: ", i["travelTo"])
        print("Travel mode: ", i["travelMode"])
        print("Travel class: ", i["travelClass"])
        print("Travel fare: ", i["travelFare"])
        print("Travel conveyance: ", i["travelConveyance"])
        print("Travel food and lodging: ", i["travelFoodLodging"])
        print("Travel incidental: ", i["travelIncidemtal"])
        print("Travel total: ", i["travelTotal"])
        print()
        print("=" * 8, "Travel details:", "=" * 8)
        print("Length of conveyances: ", len(
            i["travelDetails"]["conveyances"]))
        print("Length of food and lodgings: ", len(
            i["travelDetails"]["foodLodgings"]))
        print("Length of incidentals: ", len(
            i["travelDetails"]["incidentals"]))
        print()
        print("=" * 8, "Conveyances:", "=" * 8)
        for c, j in enumerate(i["travelDetails"]["conveyances"]):
            print("Conveyance #", c + 1)
            print("Conveyance ID: ", j["conveyanceId"])
            print("Conveyance date: ", j["conveyanceDate"])
            print("Conveyance from: ", j["conveyanceFrom"])
            print("Conveyance to: ", j["conveyanceTo"])
            print("Conveyance purpose: ", j["conveyancePurpose"])
            print("Conveyance amount: ", j["conveyanceAmount"])
            print("Conveyance bill: ", j["conveyanceBill"])
        print()
        print("=" * 8, "Food and Lodgings:", "=" * 8)
        for c, k in enumerate(i["travelDetails"]["foodLodgings"]):
            print("Food and Lodging #", c + 1)
            print("Food and Lodging ID: ", k["foodLodgingId"])
            print("Food and Lodging date: ", k["foodLodgingDate"])
            print("Food and Lodging bill no: ", k["foodLodgingBillNo"])
            print("Food and Lodging hotel: ", k["foodLodgingHotel"])
            print("Food and Lodging occupancy: ", k["foodLodgingOccupancy"])
            print("Food and Lodging amount: ", k["foodLodgingAmount"])
            print("Food and Lodging bill: ", k["foodLodgingBill"])
        print()
        print("=" * 8, "Incidentals:", "=" * 8)
        for c, l in enumerate(i["travelDetails"]["incidentals"]):
            print("Incidental #", c + 1)
            print("Incidental ID: ", l["incidentalId"])
            print("Incidental date: ", l["incidentalDate"])
            print("Incidental expense: ", l["incidentalExpense"])
            print("Incidental remarks: ", l["incidentalRemarks"])
            print("Incidental amount: ", l["incidentalAmount"])
            print("Incidental bill: ", l["incidentalBill"])


class Notification:
    """Notification class to send the email and SMS to the user"""

    def __init__(self) -> None:
        """
        Keyword arguments:
        subject -- Subject of the message
        receivers -- List of receivers
        message -- Message to be sent
        """
        # self.subject = subject
        # self.receivers = receivers
        # self.message = message

    @classmethod
    def send_email(cls, subject: str, receivers: list, message: str) -> bool:
        """Method to send the message to the user

        Return: True if the message is sent successfully else False
        """

        req_headers = {"Authorization": f"Bearer {
            AUTH_TOKEN}", "Content-Type": "application/json"}
        json_message = {"subject": subject,
                        "receiver": receivers, "message": message}
        response = requests.post(
            url=f"{NOTIFICATION_SERVER}/email",
            json=json_message,
            headers=req_headers,
        )

        print(response.status_code)
        print(response.text)

        return response.json()["status"] == "success"

    def send_sms(self, subject: str, receivers: list, message: str) -> bool:
        """Method to send the message to the user

        Return: True if the message is sent successfully else False
        """

        req_headers = {"Authorization": f"Bearer {
            AUTH_TOKEN}", "Content-Type": "application/json"}
        json_message = {"subject": subject,
                        "receiver": receivers, "message": message}
        response = requests.post(
            url=f"{NOTIFICATION_SERVER}/sms",
            json=json_message,
            headers=req_headers,
        )

        print(response.status_code)
        print(response.text)

        return response.json()["status"] == "success"
