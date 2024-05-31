import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  _SettingsPageState createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  void go_back(){
    context.go('/');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
            title: const Text("ChatGPT : Настройки"),
            backgroundColor: Colors.teal[500],
            actions: [
              TextButton(
                onPressed: go_back,
                child: const Text("Назад",
                    style: TextStyle(color: Colors.black)),
              )
            ]),
        body: const Stack(
          children: <Widget>[ Text("Это настройки")],
        ));
  }
}