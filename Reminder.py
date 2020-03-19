from core.base.model.AliceSkill import AliceSkill
from core.base.model.Intent import Intent
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Reminder(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Ask alice to remind you stuff at a given time
	"""

	DATABASE = {
		'reminders': [
			'id INTEGER PRIMARY KEY',
			'added INTEGER NOT NULL',
			'remindAt INTEGER NOT NULL',
			'reminder TEXT NOT NULL'
		]
	}

	_INTENT_ADD_REMINDER = Intent('AddReminder')
	_INTENT_RANDOM_ANSWER = Intent('RandomAnswer')


	def __init__(self):
		self._INTENTS = [
			(self._INTENT_ADD_REMINDER, self.addReminder)
		]
		super().__init__(self._INTENTS, self.DATABASE)


	def addReminder(self, session: DialogSession, **_kwargs):
		self.continueDialog(
			sessionId=session.sessionId,
			text=self.randomTalk(text='aboutWhat')
		)


	@IntentHandler('UserRandomAnswer')
	def answerReminder(self, session: DialogSession, **_kwargs):
		pass
