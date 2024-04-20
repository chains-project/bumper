Here's the updated `slice` method that should fix the error:
```java
@Override
public Slice slice(final String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name())).findFirst()), ""));
}
```
The changes made are:

* Importing the new `AuthUser` class from `com.artipie.http.auth`.
* Replacing the old `Authentication.Single` constructor with the new one that takes an `AuthUser` instead of an `Authentication.User`.
* Replacing the old `Authentication.User` constructor with the new `AuthUser` constructor that takes a name and an optional token.
* Updating the `BearerAuthScheme` constructor to use the new `AuthUser` instead of the old `Authentication.User`.

This should fix the "cannot find symbol" error related to the `User` class in the `Authentication` interface.