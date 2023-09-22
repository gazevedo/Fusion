from master.dal.DbConnection import DbConnection
from master.dal.Scripts import Scripts


class DbController:
    def __init__(self):
        self.conn = DbConnection().conn
        self.scripts = Scripts()
        self.hasAlteration = False

    def executeMigration(self):
        for script in self.scripts.list:
            result = self.executeQuery("SELECT COUNT(1) FROM MIGRATION WHERE Id = " + str(script[0]))

            if result is None or (len(result) > 0 and result[0][0] == 0):
                versao = script[0]
                script = script[1].lower()

                resultScript = self._migrationUp(script)
                if resultScript:
                    sql = f"INSERT INTO MIGRATION (ID, Date) VALUES ({versao},datetime('now'))"
                    if not self._migrationUp(sql):
                        break

    def _migrationUp(self, script):
        try:
            print(script)
            self.conn = DbConnection().conn
            cursor = self.conn.cursor()
            cursor.execute(script)
            self.conn.commit()
            self.conn.close()
            return True
        except Exception as e:
            if "table MIGRATION already exists" in str(e):
                return True
            else:
                print("Migration:", e)
                return False

    def executeQuery(self, query):
        try:
            self.conn = DbConnection().conn
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            self.conn.close()
            return result
        except Exception as e:
            print("executeQuery:", e)
            return None
