from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            if (
                response.data["detail"]
                == "Authentication credentials were not provided."
            ):
                response.data["message"] = "Token not provided"
                response.status_code = status.HTTP_400_BAD_REQUEST
                response.data.pop("detail")
            elif response.data["detail"] == "Given token not valid for any token type":
                response.data["message"] = response.data["messages"][0]["message"]
                response.data.pop("detail")
                response.data.pop("code")
                response.data.pop("messages")
            elif response.data["detail"] == "Token is invalid or expired":
                response.data["message"] = response.data["detail"]
                response.data.pop("detail")
                response.data.pop("code")
            elif response.data["detail"] == "Not found.":
                response.data["message"] = response.data["detail"]
                response.data.pop("detail")
            elif response.data["detail"] == "missing chosen_oil_pack field":
                response.data["message"] = response.data["detail"]
                response.data.pop("detail")
            elif response.data["detail"] == "Subscription item field":
                response.data["message"] = response.data["detail"]
                response.data["data"] = {}
                response.data.pop("detail")
            elif response.data["detail"] == "invalid chosen_oil_pack":
                response.data["message"] = response.data["detail"]
                response.data["data"] = {}
                response.data.pop("detail")
            elif response.data["detail"] == "User not found":
                response.data["message"] = response.data["detail"]
                response.data["data"] = {}
                response.data.pop("detail")
            elif (
                response.data["detail"]
                == "Token contained no recognizable user identification"
            ):
                response.data["message"] = response.data["detail"]
                response.data["data"] = {}
                response.data.pop("detail")
            elif (
                response.data["detail"]
                == "You do not have permission to perform this action."
            ):
                response.data["message"] = response.data["detail"]
                response.status_code = status.HTTP_400_BAD_REQUEST
                response.data.pop("detail")
            else:
                response.data["status"] = "failed"
        except:
            try:
                if (
                    response.data["authorize"]
                    == "You dont have permission for this user."
                ):
                    response.data["message"] = response.data["authorize"]
                    response.data["data"] = ""
                    response.data.pop("authorize")

                else:
                    response.data["status"] = "failed"
            except:
                response.data["status"] = "failed"

    return response
