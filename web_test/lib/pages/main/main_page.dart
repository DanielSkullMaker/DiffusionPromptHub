import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'message.dart';
import 'sign_in_dialog.dart';

class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  List<ChatMessage> messages = [
    ChatMessage(messageContent: "Hello, User!!!", isUserMessage: false)
  ];
  final TextEditingController _messageController = TextEditingController();


  void sendMessage() async {
    if (_messageController.text.isNotEmpty) {
      setState(() {
        messages.add(ChatMessage(
            messageContent: _messageController.text, isUserMessage: true));
      });
    }
    _messageController.clear();
  }

  void SignDialogShow() {
   showDialog(context: context, builder: const SignInDialog().build);
  }

  void go_settings(){
    context.go('/settings');
  }

  Widget buildMessageInput() {
    return Align(
        alignment: Alignment.bottomCenter,
        child: Expanded(
            child: Container(
                height: 100,
                color: Colors.white,
                child: Center(
                    child: SizedBox(
                        width: 700,
                        height: 50,
                        child: Row(children: <Widget>[
                          Expanded(
                            child: TextField(
                              controller: _messageController,
                              decoration: InputDecoration(
                                  hintText: "Write message...",
                                  hintStyle:
                                      const TextStyle(color: Colors.black54),
                                  focusedBorder: OutlineInputBorder(
                                    borderSide:
                                        BorderSide(color: (Colors.teal[700])!),
                                  ),
                                  enabledBorder: OutlineInputBorder(
                                    borderSide:
                                        BorderSide(color: (Colors.teal[700])!),
                                  )),
                            ),
                          ),
                          const SizedBox(width: 40),
                          FloatingActionButton(
                            onPressed: sendMessage,
                            backgroundColor: Colors.teal[500],
                            elevation: 0,
                            child: const Icon(
                              Icons.send,
                              color: Colors.white,
                              size: 18,
                            ),
                          ),
                        ]))))));
  }

  Widget buildMessages() {
    return ListView.builder(
      itemCount: messages.length,
      shrinkWrap: true,
      physics: const ScrollPhysics(),
      padding: const EdgeInsets.only(left: 10, right: 10, top: 10, bottom: 110),
      itemBuilder: (context, index) {
        return Container(
            padding:
                const EdgeInsets.only(left: 10, right: 10, top: 5, bottom: 5),
            child: Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(5),
                color: (messages[index].isUserMessage == true
                    ? Colors.teal[200]
                    : Colors.grey.shade200),
              ),
              padding: const EdgeInsets.all(15),
              child: Text(messages[index].messageContent,
                  style: const TextStyle(fontSize: 15)),
            ));
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
            title: const Text("ChatGPT"),
            backgroundColor: Colors.teal[500],
            actions: [
              IconButton(onPressed: () => {}, icon: const Icon(Icons.search)),
              SizedBox(
                  width: 200,
                  child: TextButton(
                    onPressed: SignDialogShow,
                    child: const Text("Вход/Регистрация",
                        style: TextStyle(color: Colors.black)),
                  )),
              IconButton(onPressed: go_settings, icon: const Icon(Icons.settings))
            ]),
        body: Stack(
          children: <Widget>[buildMessages(), buildMessageInput()],
        ));
  }
}
