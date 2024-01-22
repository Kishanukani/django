from django.shortcuts import render

from joblib import load

model = load("./savedModels/model.joblib")


def predict(request):
    if request.method == "POST":
        Year = request.POST["Year"]
        Present_Price = request.POST["Present_Price"]
        Kms_Driven = request.POST["Kms_Driven"]
        Fuel_Type = request.POST["Fuel_Type"]
        Seller_Type = request.POST["Seller_Type"]
        Transmission = request.POST["Transmission"]
        Owner = request.POST["Owner"]
        Y_pred = model.predict(
            [
                [
                    Year,
                    Present_Price,
                    Kms_Driven,
                    Fuel_Type,
                    Seller_Type,
                    Transmission,
                    Owner,
                ]
            ]
        )
        return render(request, "index.html", {"result": Y_pred})

    return render(request, "index.html")
