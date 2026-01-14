import os
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet

def run():
    print("   [Network] Generating P2P Diagram... ", end="", flush=True)
    
    # 저장 경로 설정 (확장자 제외)
    output_filename = "assets/fig_01_p2p_network"
    
    # show=False: 실행 시 뷰어 열지 않음
    try:
        with Diagram("Blockchain P2P Topology", show=False, filename=output_filename, direction="LR"):
            internet = Internet("Public Internet")

            with Cluster("Miner Group Asia"):
                miners_asia = [Server("Node A"), Server("Node B")]

            with Cluster("Miner Group USA"):
                miners_usa = [Server("Node C")]

            # 연결 관계 정의
            internet - Edge(color="firebrick", style="dashed") - miners_asia
            internet - miners_usa
            miners_asia[0] - miners_asia[1] # 내부 피어 연결
            
        print("✅ Done")
        
    except FileNotFoundError:
        print("\n❌ [Error] Graphviz가 설치되지 않았습니다. 'brew install graphviz'를 실행하세요.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    run()