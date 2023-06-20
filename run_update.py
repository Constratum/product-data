import pandas as pd
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json
import base64


if __name__ == "__main__":

    base64_encoded_dictstr = os.environ["creds"]

    decoded = base64.b64decode(base64_encoded_dictstr)
    datastr = decoded.decode("utf-8")
    cred_dict = json.loads(datastr)
    cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(cred)
    db = firestore.client()
    files = Path("product_information/data").glob("*.csv")  # get all csvs in your dir.

    for file in files:
        tmp = pd.read_csv(file).to_dict(orient="list")

        doc_ref = db.collection(u"calculationData").document(str(file.stem))
        doc_ref.set(tmp)
