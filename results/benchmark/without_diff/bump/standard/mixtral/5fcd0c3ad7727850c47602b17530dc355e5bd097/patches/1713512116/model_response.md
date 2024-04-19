Here's a fixed version of the method using the added library method `getClassNames()`:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(coverage.getClassNames(java.util.Collections.singleton(data.getMutatedClass()))));
}
```

The `getClassInfo()` method now receives a `Set<String>` instead of a `Set<ClassName>`. The `getClassNames()` method is used to convert the `Set<ClassName>` to a `Set<String>`.