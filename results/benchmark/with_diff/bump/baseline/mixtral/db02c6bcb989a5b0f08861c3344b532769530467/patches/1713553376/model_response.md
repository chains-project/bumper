Here is a possible patch for the failing client code:

```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(original.digest())
    );
}
```

In this patch, I removed the `false` argument from the `StringContains` constructor, as it is not needed and is causing the error. The `StringContains` matcher will, by default, look for a substring in the entire string, which is what we want in this case.