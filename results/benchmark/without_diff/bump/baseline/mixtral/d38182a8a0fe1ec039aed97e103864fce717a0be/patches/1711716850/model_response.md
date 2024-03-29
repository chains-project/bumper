Here is a fixed version of the `slice` method that should resolve the error:
```java
@Override
public Slice slice(final String action) {
    Set<Authentication.User> users = Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).collect(Collectors.toSet());
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.supplyAsync(() -> 
                users.stream()
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new Authentication.User(user.name()))
                    .findFirst()
                    .orElse(null)
            ),
            ""
        )
    );
}
```
In this version, I have created a set of `users` outside of the `BearerAuthScheme` constructor and used `CompletableFuture.supplyAsync` instead of `CompletableFuture.completedFuture` to allow the stream operation to execute asynchronously. Additionally, I have changed the `CompletableFuture` to return `null` instead of an empty `CompletableFuture` if no user is found, as this is a more idiomatic way of handling cases where no match is found.

Note that the use of `CompletableFuture.supplyAsync` may not be strictly necessary in this case, as the stream operation is not particularly expensive or time-consuming. However, I have included it here to demonstrate a general approach for handling asynchronous operations within a `CompletableFuture`. If you are confident that the stream operation will always complete quickly, you may prefer to use `CompletableFuture.completedFuture` instead.