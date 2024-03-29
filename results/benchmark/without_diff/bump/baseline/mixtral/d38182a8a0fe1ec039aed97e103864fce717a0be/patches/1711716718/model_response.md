Here is a possible patch for the code you provided:

```java
  @Override
  public Slice slice(final String action) {
    Set<Authentication.User> users = Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).collect(Collectors.toSet());
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> {
              Optional<Authentication.User> user = users.stream()
                  .filter(u -> token.equals(token(u)))
                  .findFirst();
              return CompletableFuture.completedFuture(user.map(Authentication.User::name).orElse(null));
            },
            ""
        )
    );
  }
```

I created a `users` variable to store the list of users, and then filtered the stream of users to find the one with the given token. I also added a null check in case no user is found, and return null if that's the case.