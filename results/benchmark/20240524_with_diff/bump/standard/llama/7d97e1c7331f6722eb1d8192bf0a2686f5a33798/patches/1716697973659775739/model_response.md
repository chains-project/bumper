```java
/**
 * Region.Simple can select many items.
 */
@org.junit.jupiter.api.Test
void selectsManyItems() {
    final com.jcabi.simpledb.Domain domain = this.domain();
    try {
        java.lang.Integer TEN = 10;
        for (int idx = 0; idx < TEN; ++idx) {
            domain.item(java.lang.String.format("i-%d", idx)).put("hey", "");
        }
        org.hamcrest.MatcherAssert.assertThat(domain.select(new com.amazonaws.services.simpledb.model.SelectRequest().withSelectExpression(java.lang.String.format("SELECT * FROM `%s`", domain.name())).withConsistentRead(true)), org.hamcrest.Matchers.iterableWithSize(TEN));
    } finally {
        domain.drop();
    }
}
```