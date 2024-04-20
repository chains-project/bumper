Here's a possible patch for the failing client code, taking into account the changes in the new library version:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter((user) -> token.equals(token(user)))
            .map((user) -> new AuthUser(user.name(), ""))
            .collect(Collectors.toList())), ""));
}
```
I created a new variable `AuthUser alice = new AuthUser(TestAuthentication.ALICE.name(), "");` but then removed it as it was not needed.

Instead of `new Authentication.Single(new Authentication.User(TestAuthentication.ALICE.name()), action)`, we now create `new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action)`.

The `AuthUser` class has new constructors and methods, but we can still use the existing constructor that takes a `String` for the name and an optional `String` for the context.

The `Authentication.User` class has been removed, so we replace it with `AuthUser`.

The `BearerAuthScheme` constructor takes a function that returns a `Stream<Authentication.User>`; we replace this with a function that returns a `Stream<AuthUser>`.

The `AuthUser` class has new methods, such as `name()`, but these are not used in this code.