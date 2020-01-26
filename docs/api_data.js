define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "/Users/guiconti/github/minesweeper-backend/doc/main.js",
    "groupTitle": "/Users/guiconti/github/minesweeper-backend/doc/main.js",
    "name": ""
  },
  {
    "type": "post",
    "url": "minesweeper/v1/games/",
    "title": "Create a new game",
    "name": "CreateGame",
    "group": "Game",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "seed",
            "description": "<p>Game's board generation seed.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "status",
            "description": "<p>Game's status.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "board",
            "description": "<p>Game's board.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rows",
            "description": "<p>Game's amount of rows.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "columns",
            "description": "<p>Game's amount of columns.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "mines",
            "description": "<p>Game's amount of mines.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "seed",
            "description": "<p>Game's board seed.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidDifficulty",
            "description": "<p>Difficulty sent is invalid.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidSeed",
            "description": "<p>Seed sent is invalid.</p>"
          }
        ]
      }
    },
    "filename": "./games/views.py",
    "groupTitle": "Game"
  },
  {
    "type": "patch",
    "url": "minesweeper/v1/games/:id/flag/",
    "title": "Flag a cell in the game",
    "name": "FlagCell",
    "group": "Game",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's uuid.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "x",
            "description": "<p>X Position of the desired cell to flag</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "status",
            "description": "<p>Game's status.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "board",
            "description": "<p>Game's board.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rows",
            "description": "<p>Game's amount of rows.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "columns",
            "description": "<p>Game's amount of columns.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "mines",
            "description": "<p>Game's amount of mines.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "seed",
            "description": "<p>Game's board seed.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameNotFound",
            "description": "<p>Game was not found.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidX",
            "description": "<p>X sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidY",
            "description": "<p>Y sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameOver",
            "description": "<p>You cannot change a game that is over</p>"
          }
        ]
      }
    },
    "filename": "./games/views.py",
    "groupTitle": "Game"
  },
  {
    "type": "patch",
    "url": "minesweeper/v1/games/:id/open/",
    "title": "Open a cell in the game",
    "name": "OpenCell",
    "group": "Game",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's uuid.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "x",
            "description": "<p>X Position of the desired cell to open</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "status",
            "description": "<p>Game's status.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "board",
            "description": "<p>Game's board.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rows",
            "description": "<p>Game's amount of rows.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "columns",
            "description": "<p>Game's amount of columns.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "mines",
            "description": "<p>Game's amount of mines.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "seed",
            "description": "<p>Game's board seed.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameNotFound",
            "description": "<p>Game was not found.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidX",
            "description": "<p>X sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidY",
            "description": "<p>Y sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameOver",
            "description": "<p>You cannot change a game that is over</p>"
          }
        ]
      }
    },
    "filename": "./games/views.py",
    "groupTitle": "Game"
  },
  {
    "type": "patch",
    "url": "minesweeper/v1/games/:id/question/",
    "title": "Question a cell in the game",
    "name": "QuestionCell",
    "group": "Game",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's uuid.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "x",
            "description": "<p>X Position of the desired cell to question</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "status",
            "description": "<p>Game's status.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "board",
            "description": "<p>Game's board.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rows",
            "description": "<p>Game's amount of rows.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "columns",
            "description": "<p>Game's amount of columns.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "mines",
            "description": "<p>Game's amount of mines.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "seed",
            "description": "<p>Game's board seed.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameNotFound",
            "description": "<p>Game was not found.</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidX",
            "description": "<p>X sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "InvalidY",
            "description": "<p>Y sent is not within the board's range</p>"
          },
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameOver",
            "description": "<p>You cannot change a game that is over</p>"
          }
        ]
      }
    },
    "filename": "./games/views.py",
    "groupTitle": "Game"
  },
  {
    "type": "get",
    "url": "minesweeper/v1/games/:id/",
    "title": "Retrieve a game",
    "name": "RetrieveGame",
    "group": "Game",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's uuid.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>Game's id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "status",
            "description": "<p>Game's status.</p>"
          },
          {
            "group": "Success 200",
            "type": "Array",
            "optional": false,
            "field": "board",
            "description": "<p>Game's board.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "rows",
            "description": "<p>Game's amount of rows.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "columns",
            "description": "<p>Game's amount of columns.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "mines",
            "description": "<p>Game's amount of mines.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "difficulty",
            "description": "<p>Game's difficulty.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "seed",
            "description": "<p>Game's board seed.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "GameNotFound",
            "description": "<p>Game was not found.</p>"
          }
        ]
      }
    },
    "filename": "./games/views.py",
    "groupTitle": "Game"
  }
] });
