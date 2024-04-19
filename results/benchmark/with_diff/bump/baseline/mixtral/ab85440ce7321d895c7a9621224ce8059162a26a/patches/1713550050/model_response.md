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

In this patch, I have removed the `false` argument from the `new StringContains` constructor, as it is no longer required in the new library version. This should fix the error you were seeing.