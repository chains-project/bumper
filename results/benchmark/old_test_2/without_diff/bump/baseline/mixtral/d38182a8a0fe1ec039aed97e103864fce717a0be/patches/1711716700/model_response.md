Here's a proposed patch to fix the error:

```java
  @Override
  public Slice slice(final String action) {
    Set<Authentication.User> users = Set.of(TestAuthentication.ALICE, TestAuthentication.BOB);
    BiFunction<String, Set<Authentication.User>, CompletableFuture<Authentication.User>> tokenMapper =
        (token, users) -> CompletableFuture.completedFuture(
            users.stream()
                .filter(user -> token.equals(token(user)))
                .findFirst()
                .map(user -> new Authentication.User(user.name()))
                .orElse(null));
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(tokenMapper, users, "")
    );
  }
```

In this patch, we create a new `tokenMapper` function that takes a token and a set of users, and returns a `CompletableFuture` of an `Authentication.User`. This allows us to remove the lambda expression from the `BearerAuthScheme` constructor, making the code easier to read and understand.

We also create a new `users` variable that is a set of `TestAuthentication.ALICE` and `TestAuthentication.BOB`. This allows us to pass this set to the `tokenMapper` function, making the code more concise and readable.

Note that we had to modify the `BearerAuthScheme` constructor to accept a `BiFunction` instead of a lambda expression. This is because the lambda expression was causing the compilation error.

Overall, this patch should fix the compilation error and make the code more readable and maintainable.