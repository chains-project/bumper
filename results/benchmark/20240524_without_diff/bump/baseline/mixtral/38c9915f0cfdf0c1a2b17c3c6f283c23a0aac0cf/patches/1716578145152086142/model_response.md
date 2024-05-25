Here's a patch that you can apply to fix the error:

```java
import org.cactoos.text.Texts;

// ...

@Override
public String wallets(String owner) throws IOException {
  return new JoinedText(Texts.split(get(URI.create(url + owner)), "\n"))
    .asString();
}
```

In this patch, I replaced the usage of `JoinedText` from `org.cactoos.text` package with `JoinedText` from `org.cactoos.text.Texts` package. This is because the `JoinedText` class from the `org.cactoos.text` package is no longer available, and we need to use the equivalent class from the `org.cactoos.text.Texts` package instead.