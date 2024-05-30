Here's a fixed version of the method using the new API:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(),
            coverage.getClassInfoVisitor().getClassInfo(data.getMutatedClass().asString(), new byte[0], 0));
}
```

This version uses the new `getClassInfo` method from `ClassInfoVisitor` and converts the `MutatedClass` to a string for the class name.