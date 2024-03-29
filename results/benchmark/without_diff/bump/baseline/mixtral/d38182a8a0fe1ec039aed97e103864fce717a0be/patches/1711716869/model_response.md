Here's a proposed patch to fix the error:

```java
  @Override
  public Slice slice(final String action) {
    Set<Authentication.User> users = Set.of(TestAuthentication.ALICE, TestAuthentication.BOB);
    BiFunction<String, Set<Authentication.User>, CompletableFuture<Authentication.User>> authScheme = (token, users) ->
      CompletableFuture.completedFuture(
        users.stream()
          .filter(user -> token.equals(token(user)))
          .findFirst()
          .map(user -> new Authentication.User(user.name()))
          .orElse(null)
      );
    return new DockerSlice(
      new AstoDocker(new InMemoryStorage()),
      new Permissions.Single(TestAuthentication.ALICE.name(), action),
      new BearerAuthScheme(authScheme, "", users)
    );
  }
```

In this patch, I created a new variable `users` to store the set of users, and a new variable `authScheme` to store the authentication scheme function. I also passed the `users` variable to the `BearerAuthScheme` constructor. This allows the `BearerAuthScheme` to filter the users based on the token, without relying on the `token` method from the external library.

Note that I used Java 9's `Set.of` method to create the `users` set, which is an added library method identified with `++`. If you are using an older version of Java, you can replace `Set.of` with a different method to create the set.