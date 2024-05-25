Here's a patch that you can apply to the code in order to fix the error:

```java
import org.cactoos.text.Texts;

// ...

@Override
public String ids() throws IOException {
  return new JoinedText(Texts.split(" ", new String(get("/wallets").getBody())))
    .asString();
}
```

In this patch, we've replaced the import statement for `JoinedText` with the correct import statement for `Texts`. We've also added an import statement for `Texts`.

We then use the `Texts.split()` method to split the string returned by the `get()` method on `/wallets` by spaces, and pass the resulting array to the `JoinedText` constructor.

Note that this assumes that the `get()` method returns a valid JSON string with a list of wallet IDs separated by spaces. If the format of the response has changed, you may need to modify this code accordingly.