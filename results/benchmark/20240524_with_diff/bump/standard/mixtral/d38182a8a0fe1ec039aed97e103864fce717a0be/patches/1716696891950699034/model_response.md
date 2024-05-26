Here's the proposed patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name())).findFirst()), ""));
}
```
The changes made include:

* Replacing `Authentication.User` with `AuthUser` in the `Single` constructor.
* Updating the `BearerAuthScheme` constructor to use `AuthUser` instead of `Authentication.User`.
* Importing the new `AuthUser` class and removing the unused `User` class import.

Note that these changes are based on the assumption that the `AuthUser` class has similar methods and constructors as the `Authentication.User` class. If that's not the case, the patch might need to be adjusted accordingly.