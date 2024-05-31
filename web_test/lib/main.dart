import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter_web_plugins/url_strategy.dart';
import 'package:web_test/pages/settings/settings_page.dart';
import 'package:web_test/pages/sign_up/sign_up_page.dart';
import 'pages/main/main_page.dart';

void main() {
  usePathUrlStrategy();
  runApp(const MyApp());
}

final GoRouter _router = GoRouter(
  routes: <RouteBase>[
    GoRoute(
        path: '/',
        builder: (BuildContext context, GoRouterState state) {
          return MainPage();
        },
        routes: <RouteBase>[
          GoRoute(
            path: 'settings',
            builder: (BuildContext context, GoRouterState state) {
              return SettingsPage();
            },
          ),
          GoRoute(
            path: 'sign_up',
            builder: (BuildContext context, GoRouterState state) {
              return SignUpPage();
            },
          ),
        ]),
  ],
);

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      routerConfig: _router,
    );
  }
}
