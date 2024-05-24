```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    String expected = String.format("latest: digest: %s", original.digest());
    MatcherAssert.assertThat(
        output,
        org.hamcrest.CoreMatchers.containsString(expected)
    );
}
```