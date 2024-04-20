Here's the updated code that uses the new `AuthUser` class:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(token(user)))
            .map(user -> new AuthUser(user.name()))
            .collect(Collectors.toList())), ""));
}
```
The changes I made are:

* Changed `Authentication.Single` constructor argument from `Authentication.User` to `AuthUser`.
* Updated the lambda function to return a `Stream` of `AuthUser` instead of `Authentication.User`.
* Created a new `AuthUser` instance using the `AuthUser(String, String)` constructor.

These changes should fix the "cannot find symbol" error related to the `User` class.