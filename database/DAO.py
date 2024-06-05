from database.DB_connect import DBConnect
from model.genere import Genere
from model.track import Track


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getName():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
from genre g 
"""
        cursor.execute(query)
        for row in cursor:
            result.append(Genere(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllSongs(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
from track t 
where t.GenreId = %s
        """
        cursor.execute(query, (genere, ))
        for row in cursor:
            result.append(Track(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPesati(n1, n2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.TrackId as n1, t2.TrackId as n2, t.Milliseconds as time1, t2.Milliseconds as time2  
from track t, track t2 
where t.MediaTypeId = t2.MediaTypeId and t.TrackId = %s and t2.TrackId = %s
"""
        cursor.execute(query, (n1, n2))
        for row in cursor:
            result = abs(row["time1"]-row["time2"])
        cursor.close()
        conn.close()
        print(result)
        return result
