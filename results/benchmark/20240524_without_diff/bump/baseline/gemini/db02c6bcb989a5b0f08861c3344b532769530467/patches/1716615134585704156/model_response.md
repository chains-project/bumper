```java
@Test
public void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    final String expected = String.format("latest: digest: %s", original.digest());
    assertThat(output, not(containsString(expected)));
}
```