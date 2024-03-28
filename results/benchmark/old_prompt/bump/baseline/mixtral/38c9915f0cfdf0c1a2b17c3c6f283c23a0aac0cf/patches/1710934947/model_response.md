It seems like the issue is related to the import statement of the `Joined` class from the `org.cactoos.text` package. The error message suggests that there might be a problem with the class or interface declaration.

Since I cannot see the complete code, I will assume that the necessary dependencies are included in the project configuration.

Here's the fixed failing method with the corrected import statement:

```java
import org.cactoos.text.Joined;

// ...

@Override
public ListResponse<WalletDto> list(ListRequest<WalletDto> request) {
    List<WalletDto> result = new ArrayList<>();
    for (String id : request.getIds()) {
        Optional<Wallet> wallet = wallets.get(id);
        if (wallet.isPresent()) {
            result.add(new WalletDto(wallet.get()));
        }
    }
    return new ListResponse<>(result, new Joined(", ").joining(result.stream()
            .map(WalletDto::id)
            .collect(Collectors.toList())));
}
```

In this fixed code, I have only changed the import statement to use the correct package for the `Joined` class. I assumed that the `WalletDto` and `ListResponse` classes are correctly defined and that the `wallets` object is properly initialized.

If the issue persists, please provide more context on the dependencies and the complete code for the `WalletsIn` class.