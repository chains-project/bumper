Here's the updated slice method that uses the new AuthUser class:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()),
        new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action),
        new BearerAuthScheme((token) -> CompletableFuture.completedFuture(
            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                .filter(user -> token.equals(token(user)))
                .map(user -> new AuthUser(user.name()))
                .collect(Collectors.toList())),
            "")
    );
}
```
The changes made are:

* Import the new `AuthUser` class from `com.artipie.http.auth`
* Replace `Authentication.Single` constructor argument from `Authentication.User` to `AuthUser`
* Replace `Authentication.User` constructor argument with `AuthUser` constructor
* Replace `Authentication.User` in `BearerAuthScheme` lambda argument with `AuthUser`
* Use Java 8 Streams to collect the filtered list of `AuthUser` in `BearerAuthScheme` lambda

Note: I've used Java 8 features such as lambda expressions and Streams. If your project is using an older version of Java, you might need to adjust the code accordingly.