Here's the proposed patch for the failing client code:

```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Permissions.Single(TestAuthentication.ALICE.name(), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(token(user)))
            .map(user -> new AuthUser(user.name(), user.authContext()))
            .findFirst()), ""));
}
```

The changes made include:

* Importing the new `AuthUser` class from `com.artipie.http.auth`
* Creating a new `AuthUser` instance using the new constructor that takes a `String` for both the name and auth context
* Updating the lambda expression used in the `BearerAuthScheme` constructor to create a new `AuthUser` instead of the old `User` class.