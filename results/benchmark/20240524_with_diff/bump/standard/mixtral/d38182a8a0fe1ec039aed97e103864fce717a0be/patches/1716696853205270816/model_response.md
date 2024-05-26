Here's a possible patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
        .filter(user -> token.equals(token(user)))
        .map(user -> new AuthUser(user.name(), user.authContext()))
        .findFirst()), ""));
}
```
Here are the changes I made:

* Imported the new `AuthUser` class and its `name()` and `authContext()` methods from `com.artipie.http.auth`.
* Replaced the `Authentication.Single` constructor with the new one that takes an `AuthUser` instead of an `Authentication.User`.
* Replaced the `Authentication.User` constructor with the new `AuthUser` constructor that takes a name and an auth context.
* Updated the lambda expression that creates the `AuthUser` instances to use the new `name()` and `authContext()` methods.

I hope this helps! Let me know if you have any questions or if you'd like me to clarify anything.