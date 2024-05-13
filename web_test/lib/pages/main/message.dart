class ChatMessage {
  String messageContent;
  bool isUserMessage;
  DateTime time = DateTime.now();

  ChatMessage({required this.messageContent, this.isUserMessage = true});
}
