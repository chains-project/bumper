Sure, here's a possible patch for the failing client code:
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
The change I made is to remove the `false` argument from the `StringContains` constructor, since it's not needed and is causing the compilation error.