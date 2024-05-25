Here's a possible patch for the given client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
      return null;
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```
In this patch, we first check if `classInfo` is `null` before using it. This is because the error message suggests that the symbol cannot be found, which could mean that `classInfo` is `null`. This patch should fix the error without changing the function signature or using removed library methods.