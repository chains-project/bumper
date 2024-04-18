Here's a possible patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was added in a later version of the `org.pitest.coverage.CoverageDatabase` class. This method takes a single `org.pitest.classinfo.ClassName` argument instead of a `java.util.Set<org.pitest.classinfo.ClassName>` argument. Since the `data.getMutatedClass()` method already returns a single `org.pitest.classinfo.ClassName` object, this change should still provide the correct information for the method.