class TutorialData:
    current_step = None
    tutorial_data = []

    def __init__(self):
        self.step("tutorial_welcome",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_welcome',
                          "type": 'tutorial',
                          "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "center",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "",
                          "title": "Welcome!",
                          "text": "Please follow this brief tutorial before"
                                  " we get started.",
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_welcome"
                  }
        )

        self.step("tutorial_intro",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_intro',
                          "type": 'tutorial',
                          "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "center",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "",
                          "title": "Basics",
                          "text": "In this study, we are asking you to reach a"
                                  " certain Wikipedia target article."
                                  "<br/><br/>"
                                  "For every task, you will have to reach the"
                                  " target article only by following links,"
                                  " without using a search function."
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_intro"
                  }
        )

        self.step("first_mission",
                  {
                      "message": {
                          "goal_page": {
                              "url": "wiki-schools/wp/w/Washington%252C_D.C..htm",
                              "link": "wiki-schools\\wp\\w\\Washington%252C_D.C..htm",
                              "id": 3356,
                              "name": "Washington, D.C."
                          },
                          "start_page": {
                              "url": "wiki-schools/wp/e/English_language.htm",
                              "link": "wiki-schools\\wp\\e\\English_language.htm",
                              "id": 1924,
                              "name": "English language"
                          },
                          "game_name": "PLAIN_2_21175f63-286e-476b-b202-3710806d1dde",
                          "distance": 3
                      },
                      "type": "new_game"
                  },
                  {
                      "type": "event",
                      "message": "load",
                      "url": "wiki-schools/wp/e/English_language.htm"
                  }
        )

        self.step("tutorial_landingpage",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_landingpage',
                          "type": 'tutorial', "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "top",
                                  "offset": "5rem"
                              }
                      },
                          "arrow_position": "topcenter",
                          "title": "Where am I?",
                          "text": "You are now on the start page for this task."
                                  " This bar on the top shows the details."
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_landingpage"
                  }
        )

        self.step("tutorial_startpage",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_startpage',
                          "type": 'tutorial',
                          "position": {
                              "x": {
                                  "alignment": "left",
                                  "offset": "3rem"
                              },
                              "y": {
                                  "alignment": "top",
                                  "offset": "5rem"
                              }
                          },
                          "arrow_position": "topleft",
                          "title": "Start Article",
                          "text": "This is the start page."
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_startpage"
                  }
        )

        self.step("tutorial_targetpage",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_targetpage',
                          "type": 'tutorial',
                          "position": {
                              "x": {
                                  "alignment": "right",
                                  "offset": "3rem"
                              },
                              "y": {
                                  "alignment": "top",
                                  "offset": "5rem"
                              }
                          },
                          "arrow_position": "topright",
                          "title": "Target Article",
                          "text": "And this is the article you need to find. "
                                  "You can click on this link to read the"
                                  " article for the target and get some idea of"
                                  " what you are looking for.",
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_targetpage"
                  }
        )

        self.step("tutorial_start_mission",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_start_mission',
                          "type": 'tutorial',
                          "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "center",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "",
                          "title": "Let's give it a try!",
                          "text": "Now please go ahead and try to find the"
                                  "target article by following links."
                      }
                  },
                  {
                      "type": "event",
                      "message": "load",
                      "url": "wiki-schools/wp/w/Washington%252C_D.C..htm"
                  }
        )

        self.step("tutorial_success",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_success',
                          "type": 'emphasis',
                          "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "center",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "",
                          "title": "Well Done!",
                          "text": "You found the target. "
                                  " Almost done with the tutorial!"
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_success"
                  }
        )

        self.step("second_mission",
                  {
                      "message": {
                          "goal_page": {
                              "url": "wiki-schools/wp/w/Washington%252C_D.C..htm",
                              "link": "wiki-schools\\wp\\w\\Washington%252C_D.C..htm",
                              "id": 3356,
                              "name": "Washington, D.C."
                          },
                          "start_page": {
                              "url": "wiki-schools/wp/e/English_language.htm",
                              "link": "wiki-schools\\wp\\e\\English_language.htm",
                              "id": 1924,
                              "name": "English language"
                          },
                          "game_name": "PLAIN_2_21175f63-286e-476b-b202-3710806d1dde",
                          "distance": 3
                      },
                      "type": "new_game"
                  },
                  {
                      "type": "event",
                      "message": "load",
                      "url": "wiki-schools/wp/e/English_language.htm"
                  }
        )

        self.step("tutorial_abort_button",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_abort_button',
                          "type": 'error',
                          "position": {
                              "x": {
                                  "alignment": "left",
                                  "offset": "13rem"
                              },
                              "y": {
                                  "alignment": "bottom",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "leftbottom",
                          "title": "Abort Button",
                          "text": "If you feel like you cannot find the target"
                                  "you can abort the task at any time."
                                  " Please go ahead and try this now!"
                      }
                  },
                  {
                      "type": "abort",
                      "message": None
                  }
        )

        self.step("tutorial_end",
                  {
                      "type": "tutorial",
                      "message": {
                          "name": 'tutorial_end',
                          "type": 'emphasis',
                          "position": {
                              "x": {
                                  "alignment": "center",
                                  "offset": "0"
                              },
                              "y": {
                                  "alignment": "center",
                                  "offset": "0"
                              }
                          },
                          "arrow_position": "", "title": "DONE!",
                          "text": "Thank you for completing the tutorial!"
                                  "You are now ready to start your first task."
                      }
                  },
                  {
                      "type": "tutorial_close",
                      "message": "tutorial_end"
                  }
        )

    def step(self, _step_name, _sent_message, _wait_for):
        self.tutorial_data.append(
            {"name": _step_name, "sent_message": _sent_message,
             "wait_for": _wait_for})

