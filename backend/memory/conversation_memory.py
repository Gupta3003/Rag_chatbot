class ConversationMemory:
    def __init__(self):
        self.memory = {}

    def append(self, user_id, turn):
        if user_id not in self.memory:
            self.memory[user_id] = []
        self.memory[user_id].append(turn)
        if len(self.memory[user_id]) > 10:
            self.memory[user_id] = self.memory[user_id][-10:]

    def get_history(self, user_id):
        return self.memory.get(user_id, [])
