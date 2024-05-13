import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class SignInDialog extends StatelessWidget {
  const SignInDialog({super.key});

  void sign_in() {}

  @override
  Widget build(BuildContext context) {
    return Dialog(
        //shape: const RoundedRectangleBorder(
        //    borderRadius: BorderRadius.all(Radius.circular(32.0))),
        //backgroundColor: Colors.white,
        child: Container(
            padding:
                const EdgeInsets.only(top: 50, bottom: 20, left: 60, right: 60),
            width: 400,
            height: 500,
            child: Column(
              children: <Widget>[
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
                const SizedBox(height: 100),
                Align(
                    alignment: Alignment.bottomRight,
                    child: Column(children: [
                      TextButton(
                        onPressed: sign_in,
                        style: ButtonStyle(
                            backgroundColor:
                                MaterialStateProperty.all<Color>(Colors.teal)),
                        child: const Text(
                          "Войти",
                          style: TextStyle(color: Colors.black54),
                        ),
                      ),
                      const SizedBox(height: 30),
                      TextButton(
                        onPressed: () => context.go('/sign_up'),
                        child: const Text(
                          "Регистрация",
                          style: TextStyle(color: Colors.teal),
                        ),
                      )
                    ]))
              ],
            )));
  }
}
