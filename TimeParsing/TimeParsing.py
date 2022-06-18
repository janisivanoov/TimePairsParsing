import json
from eth_utils import address
from web3 import Web3, HTTPProvider
import mysql.connector
from mysql.connector import errorcode
import hashlib
import urllib.request

# TODO: CHECK THE URL!!!
# TODO: CHECK THE URL!!!
# TODO: CHECK THE URL!!!
w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/e1aff836d3a64d6aba0f028217da381f'))
eth_key = 'X9FG4X92X5FVU75UWHT5W7VE6RDRYYNT6R'
contract = '0xa274d4daaff01e3aa710907aabdd57d036c96cec'

# Step in 100 results
maxcount = 100

#Config for database
config = {
    'user': 'db_user_1',
    'password': 'db_user_password',
    'host': 'localhost',
    'database': 'timeparsing',
    'raise_on_warnings': True
}

# ABI of contract
abiC = [
    {
        "inputs":[
            {
                "internalType":"address","name":"_factory","type":"address"
                },{"internalType":"address","name":"_WETH","type":"address"}
                ],
        "stateMutability":"nonpayable",
        "type":"constructor"
        },
        {
            "inputs":[],
            "name":"WETH",
            "outputs":
            [
                {
                    "internalType":"address","name":"","type":"address"
                    }
                ],
                "stateMutability":"view","type":"function"
                },{
                    "inputs":
                    [
                        {
                            "internalType":"address","name":"tokenA","type":"address"
                            },
                            {
                                "internalType":"address","name":"tokenB","type":"address"
                                },
                                {
                                    "internalType":"uint256","name":"amountADesired","type":"uint256"
                                    },
                                    {
                                        "internalType":"uint256","name":"amountBDesired","type":"uint256"
                                        },
                                        {
                                            "internalType":"uint256","name":"amountAMin","type":"uint256"
                                            },
                                            {
                                                "internalType":"uint256","name":"amountBMin","type":"uint256"
                                                },
                                                {
                                                    "internalType":"address","name":"to","type":"address"
                                                    },
                                                    {
                                                        "internalType":"uint256","name":"deadline","type":"uint256"
                                                        }
                                                    ],
                                                    "name":"addLiquidity",
                                                    "outputs":[
                                                        {
                                                            "internalType":"uint256","name":"amountA","type":"uint256"
                                                            },
                                                            {
                                                                "internalType":"uint256","name":"amountB","type":"uint256"
                                                                },
                                                                {"internalType":"uint256","name":"liquidity","type":"uint256"
                                                                 }
                                                                ],
                                                    "stateMutability":"nonpayable",
                                                    "type":"function"
                                                    },
                {"inputs":[
                    {
                        "internalType":"address",
                        "name":"token","type":"address"
                        },
                        {
                            "internalType":"uint256",
                            "name":"amountTokenDesired",
                            "type":"uint256"
                            },
                            {
                                "internalType":"uint256",
                                "name":"amountTokenMin",
                                "type":"uint256"
                                },
                                {
                                    "internalType":"uint256","name":"amountETHMin","type":"uint256"
                                    },{
                                        "internalType":"address","name":"to","type":"address"
                                        },{
                                            "internalType":"uint256","name":"deadline","type":"uint256"
                                            }
                                    ],
                 "name":"addLiquidityETH",
                 "outputs":[
                     {
                         "internalType":"uint256",
                         "name":"amountToken","type":"uint256"
                         },
                         {
                             "internalType":"uint256","name":"amountETH","type":"uint256"
                             },
                             {
                                 "internalType":"uint256","name":"liquidity","type":"uint256"
                                 }
                             ],
                 "stateMutability":"payable","type":"function"
                 },
                 {
                     "inputs":[],
                     "name":"factory",
                     "outputs":[
                         {
                             "internalType":"address","name":"","type":"address"
                             }
                         ],
                     "stateMutability":"view",
                     "type":"function"},
                     {"inputs":[
                         {
                             "internalType":"uint256","name":"amountOut","type":"uint256"
                             },
                             {
                                 "internalType":"uint256","name":"reserveIn","type":"uint256"
                                 },
                                 {
                                     "internalType":"uint256","name":"reserveOut","type":"uint256"
                                     }
                                 ],
                      "name":"getAmountIn","outputs":[
                          {
                              "internalType":"uint256","name":"amountIn","type":"uint256"
                              }
                          ],
                      "stateMutability":"pure","type":"function"
                      },
                      {
                          "inputs":[
                              {
                                  "internalType":"uint256","name":"amountIn","type":"uint256"
                                  },
                                  {
                                      "internalType":"uint256","name":"reserveIn","type":"uint256"
                                      },
                                      {
                                          "internalType":"uint256","name":"reserveOut","type":"uint256"
                                          }
                                      ],
                          "name":"getAmountOut",
                          "outputs":[
                              {
                                  "internalType":"uint256","name":"amountOut","type":"uint256"
                                  }
                              ],
                          "stateMutability":"pure","type":"function"
                          },
                          {
                              "inputs":[
                                  {
                                      "internalType":"uint256","name":"amountOut","type":"uint256"
                                      },
                                      {
                                          "internalType":"address[]","name":"path","type":"address[]"
                                          }
                                      ],
                              "name":"getAmountsIn",
                              "outputs":[
                                  {
                                      "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                      }
                                  ],
                              "stateMutability":"view",
                              "type":"function"
                              },
                              {
                                  "inputs":[
                                      {
                                          "internalType":"uint256","name":"amountIn","type":"uint256"
                                          },
                                          {
                                              "internalType":"address[]","name":"path","type":"address[]"
                                              }
                                          ],
                                  "name":"getAmountsOut",
                                  "outputs":[
                                      {
                                          "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                          }
                                      ],
                                  "stateMutability":"view",
                                  "type":"function"
                                  },
                                  {
                                      "inputs":[
                                          {
                                              "internalType":"uint256","name":"amountA","type":"uint256"
                                              },
                                              {
                                                  "internalType":"uint256","name":"reserveA","type":"uint256"
                                                  },
                                                  {
                                                      "internalType":"uint256","name":"reserveB","type":"uint256"
                                                      }
                                                  ],
                                      "name":"quote",
                                      "outputs":[
                                          {
                                              "internalType":"uint256","name":"amountB","type":"uint256"
                                              }
                                          ],
                                      "stateMutability":"pure","type":"function"
                                      },
                                      {
                                          "inputs":[
                                              {
                                                  "internalType":"address","name":"tokenA","type":"address"
                                                  },
                                                  {
                                                      "internalType":"address","name":"tokenB","type":"address"
                                                      },
                                                      {
                                                          "internalType":"uint256","name":"liquidity","type":"uint256"
                                                          },
                                                          {
                                                              "internalType":"uint256","name":"amountAMin","type":"uint256"
                                                              },
                                                              {
                                                                  "internalType":"uint256","name":"amountBMin","type":"uint256"
                                                                  },
                                                                  {
                                                                      "internalType":"address","name":"to","type":"address"
                                                                      },
                                                                      {
                                                                          "internalType":"uint256","name":"deadline","type":"uint256"
                                                                          }
                                                                      ],
                                          "name":"removeLiquidity",
                                          "outputs":[
                                              {
                                                  "internalType":"uint256","name":"amountA","type":"uint256"
                                                  },
                                                  {
                                                      "internalType":"uint256","name":"amountB","type":"uint256"
                                                      }
                                                  ],
                                          "stateMutability":"nonpayable","type":"function"
                                          },
                                          {
                                              "inputs":[
                                                  {
                                                      "internalType":"address","name":"token","type":"address"
                                                      },
                                                      {
                                                          "internalType":"uint256","name":"liquidity","type":"uint256"
                                                          },
                                                          {
                                                              "internalType":"uint256","name":"amountTokenMin","type":"uint256"
                                                              },
                                                              {
                                                                  "internalType":"uint256","name":"amountETHMin","type":"uint256"},
                                                                  {
                                                                      "internalType":"address","name":"to","type":"address"},
                                                                      {
                                                                          "internalType":"uint256","name":"deadline","type":"uint256"
                                                                          }
                                                                      ],
                                              "name":"removeLiquidityETH","outputs":[
                                                  {
                                                      "internalType":"uint256","name":"amountToken","type":"uint256"
                                                      },
                                                      {
                                                          "internalType":"uint256","name":"amountETH","type":"uint256"
                                                          }
                                                      ],
                                              "stateMutability":"nonpayable","type":"function"
                                              },
                                              {
                                                  "inputs":[
                                                      {
                                                          "internalType":"address","name":"token","type":"address"
                                                          },
                                                          {
                                                              "internalType":"uint256","name":"liquidity","type":"uint256"
                                                              },
                                                              {
                                                                  "internalType":"uint256","name":"amountTokenMin","type":"uint256"
                                                                  },
                                                                  {
                                                                      "internalType":"uint256","name":"amountETHMin","type":"uint256"
                                                                      },
                                                                      {
                                                                          "internalType":"address","name":"to","type":"address"
                                                                          },
                                                                          {
                                                                              "internalType":"uint256","name":"deadline","type":"uint256"
                                                                              }
                                                                          ],
                                                  "name":"removeLiquidityETHSupportingFeeOnTransferTokens",
                                                  "outputs":[
                                                      {
                                                          "internalType":"uint256",
                                                          "name":"amountETH",
                                                          "type":"uint256"
                                                          }
                                                      ],
                                                  "stateMutability":"nonpayable",
                                                  "type":"function"
                                                  },
                                                  {
                                                      "inputs":[
                                                          {
                                                              "internalType":"address","name":"token","type":"address"
                                                              },
                                                              {
                                                                  "internalType":"uint256","name":"liquidity","type":"uint256"
                                                                  },
                                                                  {
                                                                      "internalType":"uint256","name":"amountTokenMin","type":"uint256"
                                                                      },
                                                                      {
                                                                          "internalType":"uint256","name":"amountETHMin","type":"uint256"
                                                                          },
                                                                          {
                                                                              "internalType":"address","name":"to","type":"address"
                                                                              },
                                                                              {
                                                                                  "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"bool","name":"approveMax","type":"bool"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"uint8","name":"v","type":"uint8"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"bytes32","name":"r","type":"bytes32"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"bytes32","name":"s","type":"bytes32"
                                                                                                  }
                                                                                              ],
                                                      "name":"removeLiquidityETHWithPermit",
                                                      "outputs":[
                                                          {
                                                              "internalType":"uint256","name":"amountToken","type":"uint256"
                                                              },
                                                              {
                                                                  "internalType":"uint256","name":"amountETH","type":"uint256"
                                                                  }
                                                              ],
                                                      "stateMutability":"nonpayable","type":"function"
                                                      },
                                                      {
                                                          "inputs":[
                                                              {
                                                                  "internalType":"address","name":"token","type":"address"
                                                                  },
                                                                  {
                                                                      "internalType":"uint256","name":"liquidity","type":"uint256"
                                                                      },
                                                                      {
                                                                          "internalType":"uint256","name":"amountTokenMin","type":"uint256"
                                                                          },
                                                                          {
                                                                              "internalType":"uint256","name":"amountETHMin","type":"uint256"
                                                                              },
                                                                              {
                                                                                  "internalType":"address","name":"to","type":"address"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"bool","name":"approveMax","type":"bool"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"uint8","name":"v","type":"uint8"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"bytes32","name":"r","type":"bytes32"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"bytes32","name":"s","type":"bytes32"
                                                                                                      }
                                                                                                  ],
                                                          "name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
                                                          "outputs":[
                                                              {
                                                                  "internalType":"uint256","name":"amountETH","type":"uint256"
                                                                  }
                                                              ],
                                                          "stateMutability":"nonpayable",
                                                          "type":"function"
                                                          },
                                                      {
                                                          "inputs":[
                                                              {
                                                                  "internalType":"address","name":"tokenA","type":"address"
                                                                  },
                                                                  {
                                                                      "internalType":"address","name":"tokenB","type":"address"
                                                                      },
                                                                      {
                                                                          "internalType":"uint256","name":"liquidity","type":"uint256"
                                                                          },
                                                                          {
                                                                              "internalType":"uint256","name":"amountAMin","type":"uint256"
                                                                              },
                                                                              {
                                                                                  "internalType":"uint256","name":"amountBMin","type":"uint256"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"address","name":"to","type":"address"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"bool","name":"approveMax","type":"bool"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"uint8","name":"v","type":"uint8"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"bytes32","name":"r","type":"bytes32"
                                                                                                      },
                                                                                                      {
                                                                                                          "internalType":"bytes32","name":"s","type":"bytes32"
                                                                                                          }
                                                                                                      ],
                                                          "name":"removeLiquidityWithPermit",
                                                          "outputs":[
                                                              {
                                                                  "internalType":"uint256","name":"amountA","type":"uint256"
                                                                  },
                                                                  {
                                                                      "internalType":"uint256","name":"amountB","type":"uint256"
                                                                      }
                                                                  ],
                                                          "stateMutability":"nonpayable",
                                                          "type":"function"
                                                          },
                                                          {
                                                              "inputs":[
                                                                  {
                                                                      "internalType":"uint256","name":"amountOut","type":"uint256"
                                                                      },
                                                                      {
                                                                          "internalType":"address[]","name":"path","type":"address[]"
                                                                          },
                                                                          {
                                                                              "internalType":"address","name":"to","type":"address"
                                                                              },
                                                                              {
                                                                                  "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                  }
                                                                              ],
                                                              "name":"swapETHForExactTokens","outputs":[
                                                                  {
                                                                      "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                      }
                                                                  ],
                                                              "stateMutability":"payable","type":"function"
                                                              },
                                                              {
                                                                  "inputs":[
                                                                      {
                                                                          "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                          },
                                                                          {
                                                                              "internalType":"address[]","name":"path","type":"address[]"
                                                                              },
                                                                              {
                                                                                  "internalType":"address","name":"to","type":"address"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                      }
                                                                                  ],
                                                                  "name":"swapExactETHForTokens",
                                                                  "outputs":[
                                                                      {
                                                                          "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                          }
                                                                      ],
                                                                  "stateMutability":"payable","type":"function"
                                                                  },
                                                                  {
                                                                      "inputs":[
                                                                          {
                                                                              "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                              },
                                                                              {
                                                                                  "internalType":"address[]","name":"path","type":"address[]"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"address","name":"to","type":"address"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                          }
                                                                                      ],
                                                                      "name":"swapExactETHForTokensSupportingFeeOnTransferTokens",
                                                                      "outputs":[],
                                                                      "stateMutability":"payable","type":"function"
                                                                      },
                                                                      {
                                                                          "inputs":[
                                                                              {
                                                                                  "internalType":"uint256","name":"amountIn","type":"uint256"
                                                                                  },
                                                                                  {
                                                                                      "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"address[]","name":"path","type":"address[]"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"address","name":"to","type":"address"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                  }
                                                                                              ],
                                                                          "name":"swapExactTokensForETH",
                                                                          "outputs":[
                                                                              {
                                                                                  "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                                  }
                                                                              ],
                                                                          "stateMutability":"nonpayable","type":"function"
                                                                          },
                                                                          {
                                                                              "inputs":[
                                                                                  {
                                                                                      "internalType":"uint256","name":"amountIn","type":"uint256"
                                                                                      },
                                                                                      {
                                                                                          "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"address[]","name":"path","type":"address[]"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"address","name":"to","type":"address"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                      }
                                                                                                  ],
                                                                              "name":"swapExactTokensForETHSupportingFeeOnTransferTokens",
                                                                              "outputs":[],
                                                                              "stateMutability":"nonpayable",
                                                                              "type":"function"
                                                                              },
                                                                              {
                                                                                  "inputs":[
                                                                                      {
                                                                                          "internalType":"uint256","name":"amountIn","type":"uint256"
                                                                                          },
                                                                                          {
                                                                                              "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"address[]","name":"path","type":"address[]"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"address","name":"to","type":"address"
                                                                                                      },
                                                                                                      {
                                                                                                          "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                          }
                                                                                                      ],
                                                                                  "name":"swapExactTokensForTokens",
                                                                                  "outputs":[
                                                                                      {
                                                                                          "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                                          }
                                                                                      ],
                                                                                  "stateMutability":"nonpayable",
                                                                                  "type":"function"
                                                                                  },
                                                                                  {
                                                                                      "inputs":[
                                                                                          {
                                                                                              "internalType":"uint256","name":"amountIn","type":"uint256"
                                                                                              },
                                                                                              {
                                                                                                  "internalType":"uint256","name":"amountOutMin","type":"uint256"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"address[]","name":"path","type":"address[]"
                                                                                                      },
                                                                                                      {
                                                                                                          "internalType":"address","name":"to","type":"address"
                                                                                                          },
                                                                                                          {
                                                                                                              "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                              }
                                                                                                          ],
                                                                                      "name":"swapExactTokensForTokensSupportingFeeOnTransferTokens",
                                                                                      "outputs":[],
                                                                                      "stateMutability":"nonpayable",
                                                                                      "type":"function"
                                                                                      },
                                                                                      {
                                                                                          "inputs":[
                                                                                              {
                                                                                                  "internalType":"uint256",
                                                                                                  "name":"amountOut",
                                                                                                  "type":"uint256"
                                                                                                  },
                                                                                                  {
                                                                                                      "internalType":"uint256","name":"amountInMax","type":"uint256"
                                                                                                      },
                                                                                                      {
                                                                                                          "internalType":"address[]","name":"path","type":"address[]"
                                                                                                          },
                                                                                                          {
                                                                                                              "internalType":"address","name":"to","type":"address"
                                                                                                              },
                                                                                                              {
                                                                                                                  "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                                  }
                                                                                                              ],
                                                                                          "name":"swapTokensForExactETH",
                                                                                          "outputs":[
                                                                                              {
                                                                                                  "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                                                  }
                                                                                              ],
                                                                                          "stateMutability":"nonpayable",
                                                                                          "type":"function"
                                                                                          },
                                                                                          {
                                                                                              "inputs":[
                                                                                                  {
                                                                                                      "internalType":"uint256","name":"amountOut","type":"uint256"
                                                                                                      },
                                                                                                      {
                                                                                                          "internalType":"uint256","name":"amountInMax","type":"uint256"
                                                                                                          },
                                                                                                          {
                                                                                                              "internalType":"address[]","name":"path","type":"address[]"
                                                                                                              },
                                                                                                              {
                                                                                                                  "internalType":"address","name":"to","type":"address"
                                                                                                                  },
                                                                                                                  {
                                                                                                                      "internalType":"uint256","name":"deadline","type":"uint256"
                                                                                                                      }
                                                                                                                  ],
                                                                                              "name":"swapTokensForExactTokens",
                                                                                              "outputs":[
                                                                                                  {
                                                                                                      "internalType":"uint256[]","name":"amounts","type":"uint256[]"
                                                                                                      }],
                                                                                              "stateMutability":"nonpayable","type":"function"
                                                                                              },
                                                                                              {
                                                                                                  "stateMutability":"payable","type":"receive"
                                                                                                  }
]

# Contract check sum
Ccontract = w3.eth.contract(address = Web3.toChecksumAddress('0xa274d4daaff01e3aa710907aabdd57d036c96cec'), abi = abiC)

# Parameters for getLogs
params = [
  {
    "address": "0xa274d4daaff01e3aa710907aabdd57d036c96cec",
    "topics": [
      "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fd8b5e3d130840159d822"
    ]
  }
]

# Initializing MySQL connection
try:
  my_cn = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    quit()
else:
  print ("Connected to the Database")

cursor =  my_cn.cursor() 

# Function that reads first block    
def getBlock(contract):
    # read block number
    q_block = "SELECT Max(block) from main where contract = %s"
    cursor.execute(q_block, [contract])
    for (block) in cursor:
        start_block = block
    if start_block == (None,):
        start_block = (0,)
    return start_block[0]


# Function that updates main table
def updateName(domain, address, eth_contract, block):
    i_name = "insert into main (addr, amount1, amount2, block) values (%s, %s, %s, %s)"
    u_name = "update main set amount1 = %s, amount2 = %s, block=%s"
    d_name = "delete from main where addr = %s"
    if domain != "":
        if domain == "None":
            # delete name from the registry
            cursor.execute(d_name, [address])
            my_cn.commit()
        else:
            # insert or update
        
            try:
                # attempt to insert
                #TODO: CHECK HOW IT CAN BE SOLVED
                amount0 = amount0In - amount0Out
                amount1 = amount1In - amount1Out
                cursor.execute(i_name, [address, amount0, amount1, block])
            except mysql.connector.Error as err:
                # update if record is there
                if err.errno == 1062:
                    #TODO: CHECK HOW IT CAN BE SOLVED
                    amount0 = amount0In - amount0Out
                    amount1 = amount1In - amount1Out
                    cursor.execute(u_name, [amount0, amount1, block, address])
                else:
                    print (err)
                    quit()
            finally:
                my_cn.commit()

def updateNames(addresses, blocks, contracts):
    try:
            names = Ccontract.functions.getNames(addresses).call()
            ii = 0
            for n in names:
                print(addresses[ii] + "---" + n)
                updateName(str(n), str(addresses[ii]), str(contracts[ii]), str(blocks[ii]))
                ii += 1
    except BaseException as err:
            print("Exception: " + str(err))

# Read contracts into array
contracts = []
c_sql = "select address from contracts"
cursor.execute(c_sql)
for c in cursor:
    contracts.append(c)


aaa = []
bbb = []
ccc = []
i=0
for c in contracts:   
    print("Processing " + c[0])
    # Get transactions
    url = 'https://api.bscscan.com/api?module=logs&action=getLogs&fromBlock='+str(getBlock(c[0]))+'&toBlock=500000&address=0xa274d4daaff01e3aa710907aabdd57d036c96cec&topic0=0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fd8b5e3d130840159d822&apikey='+eth_key

    req = urllib.request.urlopen(url)
    resp = req.read()
    tr = json.loads(resp)
    for txh in tr["result"]:
        aaa.append(Web3.toChecksumAddress(txh["from"]))
        bbb.append(txh["blockNumber"])
        ccc.append(c[0])
        i += 1


b = 0
# loop with maxcount step
while (b+maxcount<len(aaa)):
    updateNames(aaa[b:b+maxcount], bbb[b:b+maxcount], ccc[b:b+maxcount])
    b += maxcount

updateNames(aaa[b:len(aaa)-1], bbb[b:len(bbb)-1], ccc[b:len(ccc)-1])

# Fix duplications if there is
print("Cleaning duplicates...")

# Find Duplications
c_sql = "select amount1, amount2 from duplicates"
cursor.execute(c_sql)
da = []
dn = []
for c in cursor:
    # find true address
    addr = address(c[0])
    print (c[0] + '---' + addr)
    da.append(addr)
    dn.append(c[0])

# Delete duplications
d_name = "delete from main where amount1 = %s and amount2= %s and addr != %s "
i=0
for address in da:
    cursor.execute(d_name, [ dn[i], address ])
    my_cn.commit()
    i+=1
    
# Close the cursor and the connection
cursor.close()