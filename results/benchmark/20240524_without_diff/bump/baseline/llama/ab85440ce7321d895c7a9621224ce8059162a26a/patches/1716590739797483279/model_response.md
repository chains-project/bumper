```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    String expectedOutput = String.format("latest: digest: %s", original.digest());
    MatcherAssert.assertThat(output, CoreMatchers.containsString(expectedOutput));
}
```