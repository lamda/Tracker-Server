# -*- coding: utf-8 -*-

import unidecode

import uuid
import DbConnector


database_connection = DbConnector.DbConnector()


class User:

    def __init__(self, _game):
        self.game = _game
        self.attributes = dict()
        self.attributes['id'] = [str(uuid.uuid4()), True]
        self.attributes['name'] = ["guest", True]
        self.attributes['age'] = [1, True]
        self.attributes['education'] = ["", True]
        self.attributes['language'] = ["", False]
        self.attributes['eyesight'] = [0, True]
        self.attributes['sleep'] = [1, True]
        self.attributes['caffeine'] = [0, True]
        self.attributes['pc_experience'] = [0, True]
        self.attributes['web_experience'] = [0, False]
        self.attributes['played_before'] = [0, True]

        self.complete = False

    def set_attribute(self, _message_payload):
        value = _message_payload['value']
        print(_message_payload)
        if isinstance(_message_payload['value'], bool):
            value = int(_message_payload['value'])
            print("converting")

        self.attributes[_message_payload['name']][0] = value
        self.attributes[_message_payload['name']][1] = True
        self.request_feature()

    def get_attributes(self):
        return self.attributes

    def load_user(self, _user_id):
        user_data = database_connection.execute("SELECT * "
                                                "FROM users "
                                                "WHERE user_id = %s "
                                                "LIMIT 1",
                                                _user_id,
                                                "SELECT")[0]
        print("USER DATA: ")
        print(user_data)

        self.attributes['id'][0] = user_data['user_id']
        self.attributes['id'][1] = True
        self.attributes['name'][0] = user_data['name']
        self.attributes['name'][1] = True
        self.attributes['age'][0] = user_data['user_id']
        self.attributes['age'][1] = True
        self.attributes['education'][0] = user_data['education']
        self.attributes['education'][1] = True
        self.attributes['language'][0] = user_data['language']
        self.attributes['language'][1] = True
        self.attributes['eyesight'][0] = user_data['eyesight']
        self.attributes['eyesight'][1] = True
        self.attributes['sleep'][0] = user_data['sleep']
        self.attributes['sleep'][1] = True
        self.attributes['caffeine'][0] = user_data['caffeine']
        self.attributes['caffeine'][1] = True
        self.attributes['pc_experience'][0] = user_data['pc_experience']
        self.attributes['pc_experience'][1] = True
        self.attributes['web_experience'][0] = user_data['web_experience']
        self.attributes['web_experience'][1] = True
        self.attributes['played_before'][0] = user_data['played_before']
        self.attributes['played_before'][1] = True
        self.complete = True
        self.game.session_start()

    def new_user(self):
        print("NEW USER!")
        self.request_feature()

    def store_user(self):
        database_connection.execute("INSERT INTO users "
                                    "(user_id, name, age, education, language, eyesight, caffeine, sleep, pc_experience, web_experience, played_before) "
                                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (self.attributes['id'][0],
                                     self.attributes['name'][0],
                                     self.attributes['age'][0],
                                     self.attributes['education'][0],
                                     self.attributes['language'][0],
                                     self.attributes['eyesight'][0],
                                     self.attributes['caffeine'][0],
                                     self.attributes['sleep'][0],
                                     self.attributes['pc_experience'][0],
                                     self.attributes['web_experience'][0],
                                     self.attributes['played_before'][0]
                                    ),
                                    "INSERT")
        database_connection.commit()

        self.game.session_start()

    def request_feature(self):
        if not self.attributes['name'][1]:
            self.game.socket.write_json_message("feature_request", ("What's your name?", "name", "string"))
            return
        elif not self.attributes['age'][1]:
            self.game.socket.write_json_message("feature_request", ("how old are you?", "age", "int"))
            return
        elif not self.attributes['education'][1]:
            self.game.socket.write_json_message("feature_request", ("What is your level of education?", "education", "string"))
            return
        elif not self.attributes['language'][1]:
            self.game.socket.write_json_message("feature_request", ("Is English your native language OR is English a local language at your place of residence?", "language", "bool"))
            return
        elif not self.attributes['eyesight'][1]:
            self.game.socket.write_json_message("feature_request", ("Do you wear glasses?", "eyesight", "bool"))
            return
        elif not self.attributes['sleep'][1]:
            self.game.socket.write_json_message("feature_request", ("Did you have enough sleep last night?", "sleep", "bool"))
            return
        elif not self.attributes['caffeine'][1]:
            self.game.socket.write_json_message("feature_request", ("Did you recently have some coffee or any other caffeine containing beverage?", "caffeine", "bool"))
            return
        elif not self.attributes['pc_experience'][1]:
            self.game.socket.write_json_message("feature_request", ("How would your rate your experience in using a computer?", "pc_experience", "range", (0, 10)))
            return
        elif not self.attributes['web_experience'][1]:
            self.game.socket.write_json_message("feature_request", ("How do you rate your experience with the Web?", "web_experience", "range", (0, 10)))
            return
        elif not self.attributes['played_before'][1]:
            self.game.socket.write_json_message("feature_request", ("Have you played this before?", "played_before", "bool"))
            return
        else:
            self.complete = True
            self.store_user()
