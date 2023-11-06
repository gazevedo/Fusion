import cv2
import urllib
import requests
import numpy as np
import numpy as np
from requests.auth import HTTPBasicAuth

from master.controller.DbController import DbController
from master.view.FrmLogin import FrmLogin
from master.view.FrmPrincipal import FrmPrincipal


def main():
    dbcontroller = DbController()
    dbcontroller.executeMigration()
    FrmPrincipal()

if __name__ == "__main__":
    main()