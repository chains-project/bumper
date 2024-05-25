Here's a possible patch for the failing client code:
```java
  @Override
  public Slice slice(final String action) {
    BiFunction<String, Map<String, User>, Optional<User>> tokenValidator =
        (token, users) -> users.values().stream()
            .filter(user -> token.equals(token(user)))
            .findFirst();
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                tokenValidator.apply(token, Map.of(
                    TestAuthentication.ALICE.name(), TestAuthentication.ALICE,
                    TestAuthentication.BOB.name(), TestAuthentication.BOB
                ))
                .map(User::name)
                .orElse(null)
            ),
            ""
        )
    );
  }
```
In this patch, I created a new variable `tokenValidator` that takes a token and a map of users, and returns an `Optional<User>` representing the user associated with the token, if any. This variable is then used in the `BearerAuthScheme` constructor to validate the token.

Note that I used the `Map.of` method introduced in Java 9 to create the `users` map. If your environment doesn't support Java 9, you can use a different way to create the map, such as:
```java
Map<String, User> users = new HashMap<>();
users.put(TestAuthentication.ALICE.name(), TestAuthentication.ALICE);
users.put(TestAuthentication.BOB.name(), TestAuthentication.BOB);
```
This patch assumes that the `User` class has a `name()` method that returns the user name as a string. If this is not the case, you may need to adjust the code accordingly.