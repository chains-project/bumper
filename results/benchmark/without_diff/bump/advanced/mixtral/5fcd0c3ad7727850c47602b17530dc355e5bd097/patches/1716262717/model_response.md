Here is a fixed version of the method using the new method `getClassInfos` introduced in `CoverageDatabase`:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfos(java.util.Collections.singleton(data.getMutatedClass())));
}
```
The new method `getClassInfos` takes a `Set<ClassName>` instead of a single `ClassName`, so I updated the argument accordingly.