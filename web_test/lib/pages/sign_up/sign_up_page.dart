import 'package:flutter/material.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});

  @override
  _SignUpPageState createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  get sign_up => null;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("ChatGPT : Регистрация"),
          backgroundColor: Colors.teal[500],
        ),
        body: Center(
            child: SizedBox(
                width: 400,
                child: Column(
                  children: <Widget>[
                    const SizedBox(
                      height: 30,
                    ),
                    const Text(
                      "Войти",
                      style: TextStyle(fontSize: 20),
                    ),
                    const SizedBox(height: 60),
                    const TextField(
                        cursorColor: Colors.teal,
                        decoration: InputDecoration(
                          hintText: "Логин",
                          hintStyle: TextStyle(color: Colors.black54),
                        )),
                    const TextField(
                        cursorColor: Colors.teal,
                        decoration: InputDecoration(
                          hintText: "Пароль",
                          hintStyle: TextStyle(color: Colors.black54),
                        )),
                    const TextField(
                        cursorColor: Colors.teal,
                        decoration: InputDecoration(
                          hintText: "Почта",
                          hintStyle: TextStyle(color: Colors.black54),
                        )),
                    const SizedBox(height: 100),
                    Align(
                        alignment: Alignment.bottomRight,
                        child: Column(children: [
                          TextButton(
                            onPressed: sign_up,
                            style: ButtonStyle(
                                backgroundColor:
                                    MaterialStateProperty.all<Color>(
                                        Colors.teal)),
                            child: const Text(
                              "Зарегистрироваться",
                              style: TextStyle(color: Colors.black54),
                            ),
                          )
                        ]))
                  ],
                ))));
  }
}
