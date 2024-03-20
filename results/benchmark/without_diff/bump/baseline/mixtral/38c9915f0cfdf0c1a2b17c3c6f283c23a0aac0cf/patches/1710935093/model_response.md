It seems like the issue is related to the imported class `org.cactoos.text.Joined` which might not be available in the current version of the dependency. To fix this issue, we can use the Java 8 Streams API to join the strings. Here's the updated code for the failing method:

```java
@Override
public String deposit(Collection<String> walletIds) throws IOException {
    return walletIds.stream()
        .map(this::wallet)
        .map(Wallet::deposit)
        .collect(Collectors.joining("\n"));
}
```

This code does the same thing as the original code, but uses Java 8 Streams API to join the strings instead of the `Joined` class from the `cactoos` library. This should fix the error and make the code work as expected.