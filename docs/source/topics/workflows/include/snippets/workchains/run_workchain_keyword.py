# -*- coding: utf-8 -*-
from aiida.engine import run
from aiida.orm import Int

result = run(AddAndMultiplyWorkChain, a=Int(1), b=Int(2), c=Int(3))  # noqa: F821
